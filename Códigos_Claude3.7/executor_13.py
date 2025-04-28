class CommandExecutor:
    def __init__(self):
        pass

    def run_command(self, command):
        import subprocess

        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {
                'stdout': result.stdout.decode('utf-8'),
                'stderr': result.stderr.decode('utf-8'),
                'returncode': result.returncode
            }
        except subprocess.CalledProcessError as e:
            return {
                'stdout': e.stdout.decode('utf-8'),
                'stderr': e.stderr.decode('utf-8'),
                'returncode': e.returncode
            }