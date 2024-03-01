""" Custom filters for Ansible."""

# Creates a base64 tarball from a list of file descriptions
def files2tar(files, compress='gz',
                owner='root', group='root',
                file_mode=0o0644, dir_mode=0o0755):

    import tarfile
    import io
    import base64
    import time
    import dateutil.parser

    tar_obj = io.BytesIO()

    with tarfile.open(fileobj=tar_obj, mode=f"w:{compress}") as tar:
        for file in files:

            file_type = file.get('type', 'regular')

            if 'mtime' in file:
               mtime = dateutil.parser.parse(file['mtime']).timestamp()
            else:
               mtime = int(time.time())

            tarinfo = tarfile.TarInfo(file['path'])
            tarinfo.uname = file.get('owner', owner)
            tarinfo.gname = file.get('group', group)
            tarinfo.mtime = mtime

            if file_type == 'regular':
                tarinfo.mode = file.get('mode', file_mode)
                tarinfo.size = len(file['content'])
                tar.addfile(tarinfo, io.BytesIO(file['content'].encode('utf-8')))

            elif file_type == 'directory':
                tarinfo.type = tarfile.DIRTYPE
                tarinfo.mode = file.get('mode', dir_mode)
                tar.addfile(tarinfo)

    return base64.b64encode(tar_obj.getbuffer())


class FilterModule(object):
    def filters(self):
        return {
            'files2tar': files2tar
        }
