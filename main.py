import argparse
import hashlib
from colorama import Fore, init
import sys

init(autoreset=True)
class robloxpro:

    @staticmethod
    def hashing(password: str, algorithm: str) -> str:
        try:
            dick = hashlib.new(algorithm)
            dick.update(password.encode('utf-8'))
            return dick.hexdigest()
        except ValueError as e:
            print(e)
            return None

def sex():
    sa = [
        'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512',
        'blake2b', 'blake2s', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512',
        'shake_128', 'shake_256', 'whirlpool', 'ripemd160'
    ]

    par = argparse.ArgumentParser(description=f"{Fore.CYAN}suck my dick")
    par.add_argument('-s', '--string', type=str, help=f"{Fore.YELLOW}Şifrelenecek metin.")
    par.add_argument('-a', '--algorithm', type=str, choices=sa,)

    holymoly = par.parse_args()

    if not holymoly.string or not holymoly.algorithm:
        print(f"{Fore.YELLOW}alg list: {', '.join(sa)}")
        print(f"{Fore.RED}usage: python main.py -s <str> -a <alg>")
        sys.exit(1)

    result = robloxpro.hashing(holymoly.string, holymoly.algorithm)

    if result:
        print(f"{Fore.LIGHTGREEN_EX}out: ({holymoly.algorithm}): {Fore.MAGENTA}{result}")
    else:
        print(f"{Fore.CYAN} use your brain")


if __name__ == "__main__":
    sex()
