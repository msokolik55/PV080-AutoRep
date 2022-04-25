# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
import base64
import subprocess
import pickle
import flask

# Input injection


def transcode_file(_, filename):
    """Transcode the file"""
    command = 'ffmpeg -i "{source}" output_file.mpg'\
        .format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!


# Assert statements
def assert_statements(_, user):
    """Assert statements"""
    assert user.is_admin, 'user does not have access'
    # secure code...


# Pickles
class RunBinSh(object):
    """Class for BinSh"""

    def __reduce__(self):
        """Reduce"""
        return (subprocess.Popen, (('/bin/sh',),))


def import_urlib_version(version):
    """Import urlib"""
    exec("import urllib%s as urllib" % version)


@app.route('/')
def index():
    """Run flask"""
    module = flask.request.args.get("module")
    import_urlib_version(module)


print(base64.b64encode(pickle.dumps(RunBinSh())))
