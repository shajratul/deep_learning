# NVidia DGX Quick Start Guide
This template is intended to help first time users of the AI Lab DGX server.

1. Verify that you can log in to the educational cluster using the user name and
password you received. The clusters are available via SSH. If you are
travelling, you might need to use a VPN connection.

The recommended Windows client is Putty. From a Mac, you can use ssh from the
Terminal application (found under /Applications/Utilities). Linux users can run
ssh from any terminal or console.

To access the Educational cluster, use:

```
ssh -l username seawulf.uri.edu
```

The first time you log in you will be asked to reset your password.

2.



### GitHub notes
I had to do the following in order to allow GithHub authentication (maybe because I'm using and organizational repo?):

```
git remote set-url origin "https://hdekk@github.com/uri-ai-lab/dgx-template.git"
unset SSH_ASKPASS
git push origin master
```

For convenience I added unset SSH_ASKPASS to my .bashrc
