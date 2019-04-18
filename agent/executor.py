import subprocess
import tempfile
from utils import getlogger

logger = getlogger(__name__, '/Users/lixin/{}.log'.format(__name__))


class Executor(object):

    def run(self, script: str, timeout=5):
        """
        执行器,执行脚本的方法
        :param script:  脚本
        :param timeout:  超时时间
        :return: 返回 tuple，（状态码,输出信息)
        """
        with tempfile.TemporaryFile() as f:  # 返回一个临时文件对象
            logger.info(script)
            proc = subprocess.Popen(script, shell=True, stderr=f, stdout=f)
            try:
                code = proc.wait(int(timeout))
                logger.info(code)
                f.seek(0)
                if code == 0:
                    txt = f.read()
                else:
                    txt = f.read()
                logger.info('<{} {}>'.format(code, txt))
                return code, txt
            except Exception as e:
                logger.error(e)
                return 1, ''


if __name__ == '__main__':
    exec = Executor()
    ret = exec.run('sleep 10', timeout=5)
    print(ret)
