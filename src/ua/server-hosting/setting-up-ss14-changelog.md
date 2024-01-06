# Setting up SS14.Changelog

## Main setup

See the repo: https://github.com/space-wizards/SS14.Changelog

## RSS feed

The publishing system can automatically publish the changelog to an RSS feed. This is done from [`actions_changelog_rss.py`](https://github.com/space-wizards/space-station-14/blob/master/Tools/actions_changelog_rss.py) which is ran from the [publishing workflow](https://github.com/space-wizards/space-station-14/blob/master/.github/workflows/publish.yml).

### Server setup

The resulting RSS file must be hosted on a separate server, accessible via SFTP. I recommend setting up an SFTP-only chrooted user. If you know how to do this you probably don't need to look very hard at this.

```shell
# Create a group for SFTP-only users
groupadd sftp-only
# Create changelog user
useradd changelog-rss --groups sftp-only --create-home

# Create directory for chrooted sftp
mkdir --parents /var/sftp/home/changelog-rss
chown changelog-rss: /var/sftp/home/changelog-rss

# Set up SSH key for user
mkdir /home/changelog-rss/.ssh
ssh-keygen -t ed25519 -f changelog_key -N ""
cat changelog_key.pub >> /home/changelog-rss/.ssh/authorized_keys
# Save changelog_key, you'll need it for GitHub-side setup.
chown -R changelog-rss: /home/changelog-rss/.ssh

# (example, depends on what web server you want to use)
# Give nginx access to the upload directory
setfacl -m u:nginx:rx /var/sftp/home/changelog-rss
```

You will also need to add the following to `/etc/ssh/sshd_config`:

```
Subsystem sftp internal-sftp

Match Group sftp-only
    ChrootDirectory /var/sftp
    X11Forwarding no
    AllowTcpForwarding no
    AllowAgentForwarding no
    ForceCommand internal-sftp
```

You'll still need to make sure the changelog file is exposed through a web server somwhere. I'll leave that up to you. Whatever you do, make sure that your web server reports the file's `Content-Type` as `application/rss+xml`.

```admonish warning
The SSH key MUST be ed25519. I couldn't be bothered to make the script more flexible.
```

### GitHub setup

In the official publishing workflow, `actions_changelog_rss.py` automatically starts running once the `CHANGELOG_RSS_KEY` secret is set on GitHub. This should be the private key that will allow you to connect over SFTP.

Before you set that however, there are still some changes you should make to `actions_changelog_rss.py`:

```python
# Change these to suit your server settings
# https://docs.fabfile.org/en/stable/getting-started.html#run-commands-via-connections-and-run
SSH_HOST = "centcomm.spacestation14.io"
SSH_USER = "changelog-rss"
SSH_PORT = 22
RSS_FILE = "changelog.xml"
HOST_KEYS = [
    "AAAAC3NzaC1lZDI1NTE5AAAAIEE8EhnPjb3nIaAPTXAJHbjrwdGGxHoM0f1imCK0SygD"
]

# RSS feed parameters, change these
FEED_TITLE       = "Space Station 14 Changelog"
FEED_LINK        = "https://github.com/space-wizards/space-station-14/"
FEED_DESCRIPTION = "Changelog for the official Wizard's Den branch of Space Station 14."
FEED_LANGUAGE    = "en-US"
FEED_GUID_PREFIX = "ss14-changelog-wizards-"
FEED_URL         = "https://central.spacestation14.io/changelog.xml"
```

* You should set the `SSH_` parameters to whatever connection parameters you need to connect via SSH.
* `RSS_FILE` is the name of the destination file in the SFTP directory.
* `HOST_KEYS` must contain the ed25519 host key of your destination system. You can find it at `/etc/ssh/ssh_host_ed25519_key.pub`. Cut off the starting `ssh-ed25519` bit.
* `FEED_` parameters all change the contents of the RSS feed. You should probably change these to make them distinct from the ones used by Wizard's Den.

### Custom XML data

The RSS feed created contains both a normal HTML-based description of the changes, as well as some more structured information from the source changelog, that can be displayed by specialized tools. This data is all under the `https://spacestation14.com/changelog_rss` XML namespace.

A quick summary of the data:
* An `<item>` contains a `ss14:from-id` and `ss14:to-id` to describe the range of changelogs covered by an RSS item.
* Each RSS item can contain a series of `<ss14:entry>` elements containing the entries making up the RSS item.