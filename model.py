from gpiozero import LED
import words

led=LED(27)

class Word():
    def __init__(self):
        self._on_start=led.on
        self._on_stop=led.off
        self._char_seq=()

    def make(self,word):
        result=words.build_word(word)
        self._char_seq=result

    def pronounce(self):
        if self._char_seq:
            for r in self._char_seq:
                r(self._on_start,on_end_func=self._on_stop)

