# Custom ansible filters


## Container file system overlay through environment variable

This is useful when your container requires configuration files, but you don't
want to mount a volume (for whatever reason).

You supply a list of file descriptions, which includes (at least) their path and content.
Optionally you can configure the owner, group, mode, and mtime.
Containing directories are automatically created.

You can try it out using the [example playbook](playbook_files2tar.yml).

```shell
# Set up venv and install collections
./setup.sh

# Run the playbook on a host that has docker installed (default localhost)
ansible-playbook playbook_files2tar.yml
```
