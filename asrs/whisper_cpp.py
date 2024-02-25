from typing import Callable
import os
import subprocess
import common

def whisper_cpp_clo() -> Callable:
    whisper_cpp_command = os.environ.get("ASR_WHISPER_CPP_COMMAND")
    whisper_cpp_model = os.environ.get("ASR_WHISPER_CPP_MODEL")
    wav_temp_file = "temp.wav"
    output_file = "temp.wav.txt"
    @common.wrap_log_ts
    def whisper_cpp() -> str:
        command = f"{whisper_cpp_command} -m {whisper_cpp_model} -l zh -f ./{wav_temp_file} -otxt"
        result = subprocess.run(command, shell=True, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return open(output_file, "r").read()
        raise Exception(result.stderr.decode("utf-8"))
    return whisper_cpp



if __name__ == '__main__':
    whisper_cpp = whisper_cpp_clo()
    whisper_cpp()