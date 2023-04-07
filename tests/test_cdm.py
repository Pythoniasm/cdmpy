# Author: Lu Xu <oliver_lew@outlook.com">
# License: MIT
# Original Repo: https://github.com/OliverLew/fio-cdm
# Packaging: https://github.com/Pythoniasm/fio-cdm

from fio_cdm import Job, get_parser
from subprocess import Popen, PIPE


def test_job():
    parser = get_parser()
    args = parser.parse_args()

    job = Job(**vars(args))
    job.create_job("rnd", 1, 1)
    job.run()


def test_entrypoint():
    command = "fio-cdm -s 1m"
    res = Popen(command.split(" "), stdout=PIPE)
    output, _ = res.communicate()
    assert output != ""
