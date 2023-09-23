
import pytest
from project import *
def main():
    test_check_encrypt_decrypt()
    test_encrypt()
    test_decrypt

def test_encrypt():
    assert encrypt('cs50') == '-.-. ... ..... -----'
    assert encrypt('David J. Malan') == '-.. .- ...- .. -..  .--- .-.-.-  -- .- .-.. .- -.'
    assert encrypt('Manoj Sharma') == '-- .- -. --- .---  ... .... .- .-. -- .-'
    assert encrypt('cs50 python') == '-.-. ... ..... -----  .--. -.-- - .... --- -.'
    assert encrypt('morse_code') == '-- --- .-. ... . ..--.- -.-. --- -.. .'
    assert encrypt('malan@harvard.edu') == '-- .- .-.. .- -. .--.-. .... .- .-. ...- .- .-. -.. .-.-.- . -.. ..-'

def test_decrypt():
    assert decrypt('-.-. ... ..... -----') == 'Cs50'
    assert decrypt('-.. .- ...- .. -..  .--- .-.-.-  -- .- .-.. .- -.') == 'David J. Malan'
    assert decrypt('-- .- -. --- .---  ... .... .- .-. -- .-') == 'Manoj Sharma'
    assert decrypt('-.-. ... ..... -----  .--. -.-- - .... --- -.') == 'Cs50 Python'


def test_check_encrypt_decrypt():
    assert check_encrypt_decrypt("abc") == False
    assert check_encrypt_decrypt("-.-. ... .... .-----") == True
    with pytest.raises(SystemExit) as e:
        check_encrypt_decrypt("#")
        check_encrypt_decrypt("%")
        check_encrypt_decrypt("^")
        check_encrypt_decrypt("*")
        check_encrypt_decrypt(">")
        check_encrypt_decrypt("[")
        check_encrypt_decrypt("]")
        check_encrypt_decrypt("{")
        check_encrypt_decrypt("}")
        check_encrypt_decrypt(">")
        check_encrypt_decrypt("<")
    assert str(e.value) == "Invalid characters present in the string"

if __name__ == "__main__":
    main()
