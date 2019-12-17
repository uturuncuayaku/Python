"""
What is this pattern about?
A Factory is an object for creating other objects.

Whats does this examply do?
The code shows a way to localize words in two languages:English and Greek. "get_localizer" is the factory function that constructs a localizer depending on the language chosen. The localizer object will be an instance from a different class according to the language localized. Hower, the main code does not have to worry about which lolocalizer will be instantiated, since the method localize will be called in the same way independently of the language. 

Where can the pattern be used practically?
The Factory Method can be seen in the popular web framework Django: django.wikispaces.asu.edu
For example, in a contact form of a web page, the subject and the message fields are created using the same form factory(CharField()), even though they have different implementations accord to their purposes.

TL;DR Creates objects without having to specify the exact class
"""
class GreekLocalizer:
    """A simple localizer a la gettext"""
    def __init__(self):
        self.translations = {"dog": "σκύλος", "cat":"γάτα"}
    def localize(self,msg):
        """ We'll punt if we dont have a translation"""
        return self.translations.get(msg,msg)
class EnglishLocalizer:
    """Simply echoes the message"""
    def localize(self,msg):
        return msg
def get_localizer(language="English"):
    """Factory"""
    localizers = {"English" : EnglishLocalizer,
                "Greek": GreekLocalizer,
            }
    return localizers[language]()
def main():
    """
    # create our localizers
    >>> e, g = get_localizers(language="English"), get_localizer(language="Greek")
    # Localize some text
    >>> for msg in "dog parrot cat bear".split():
... print(e.localize(msg), g.localize(msg)
    dog σκύλος
    parrot parrot
    cat γάτα
    bear bear
"""

if __name__=="__main__":
    import doctest
    doctest.testmod()

