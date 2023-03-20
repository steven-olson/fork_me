from flask import Flask, redirect
import os
from werkzeug.wrappers.response import Response

flask_app = Flask(__name__)


DEFAULT_URL = "https://github.com/steven-olson/fork_me"


@flask_app.route("/fork_me")
def fork_this_project() -> Response:
    """
    Simple flask endpoint which redirects caller to a
    certain github repo fork page.

    :return: None
    """
    return redirect(_get_target_url(), code=302)


def _get_target_url() -> str:
    """
    Build target url fork page of what we want to fork.
    :return:
    """
    return f"{os.environ.get('TARGET_URL')}/fork"\
        if os.environ.get("TARGET_URL")\
        else f"{DEFAULT_URL}/fork"


if __name__ == "__main__":
    flask_app.run()
