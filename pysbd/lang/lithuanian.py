import re
from pysbd.between_punctuation import BetweenPunctuation
from pysbd.lang.common import Common, Standard
from pysbd.utils import Rule, Text
from pysbd.punctuation_replacer import replace_punctuation


class Lithuanian(Common, Standard):
    iso_code = "lt"

    class Abbreviation(Standard.Abbreviation):
        ABBREVIATIONS = [
            "a",
            "adv",
            "a. k",
            "akad",
            "aklg",
            "akt",
            "al",
            "angl",
            "aps",
            "apsk",
            "apyg",
            "a. s",
            "asist",
            "asmv",
            "atsak",
            "aut",
            "avd",
            "biol",
            "b. k",
            "bkl",
            "bot",
            "bt",
            "buv",
            "chem",
            "d",
            "dail",
            "dek",
            "dėst",
            "dir",
            "dirig",
            "doc",
            "dr",
            "drp",
            "dš",
            "e",
            "egz",
            "eil",
            "ekon",
            "el",
            "el. p",
            "e. p",
            "etc",
            "ež",
            "fak",
            "faks",
            "filol",
            "filos",
            "g",
            "G",
            "gen",
            "geol",
            "gerb",
            "gim",
            "gv",
            "gyd",
            "įl",
            "Įn",
            "insp",
            "inž",
            "ir pan",
            "ir t. t",
            "istor",
            "J. E",
            "J. Em",
            "k",
            "K",
            "k. a",
            "kand",
            "kat",
            "kl",
            "kln",
            "kn",
            "koresp",
            "kpt",
            "kr",
            "kt",
            "kun",
            "kyš",
            "l. e. p",
            "ltn",
            "m",
            "mat",
            "m. e",
            "med",
            "mėn",
            "mgr",
            "mjr",
            "mln",
            "mlrd",
            "m. m",
            "mok",
            "mokyt",
            "mot",
            "mst",
            "mstl",
            "N",
            "nkt",
            "ntk",
            "p",
            "pav",
            "pavad",
            "p. d",
            "pirm",
            "pl",
            "plg",
            "plk",
            "p. m. e",
            "pr",
            "pranc",
            "pr. Kr",
            "prof",
            "prok",
            "prot",
            "psl",
            "pss",
            "pšt",
            "pvz",
            "r",
            "red",
            "rš",
            "s",
            "sąs",
            "sąsk",
            "sav",
            "saviv",
            "sekr",
            "sen",
            "sk",
            "skg",
            "skv",
            "skyr",
            "š. m",
            "šnek",
            "šv",
            "sp",
            "spec",
            "sr",
            "str",
            "stud",
            "t",
            "techn",
            "tel",
            "teol",
            "tir",
            "t. p",
            "tūkst",
            "t. y",
            "up",
            "upl",
            "V",
            "vad",
            "ved",
            "vet",
            "virš",
            "vlsč",
            "vnt",
            "vs",
            "Vt",
            "Vt",
            "vtv",
            "vv",
            "vyr",
            "vyresn",
            "žml",
            "zool",
            "žr",
            "ž. ū",
        ]
        PREPOSITIVE_ABBREVIATIONS = ["doc", "prof", "dr"]
        NUMBER_ABBREVIATIONS = ["Nr"]

    class BetweenPunctuation(BetweenPunctuation):
        BETWEEN_LITHUANIAN_DOUBLE_QUOTES_REGEX = r"„(?>[^“\\]+|\\{2}|\\.)*“"

        class DialogRules:
            QuestionExclamationMarkDialogRule = Rule(r"\?\!(?=\s–\s[a-ž])", "&ᓷ&&ᓴ&")
            ExclamationMarkDialogRule = Rule(r"\!(?=\s–\s[a-ž])", "&ᓴ&")
            QuestionMarkDialogRule = Rule(r"\?(?=\s–\s[a-ž])", "&ᓷ&")
            All = [
                QuestionExclamationMarkDialogRule,
                ExclamationMarkDialogRule,
                QuestionMarkDialogRule,
            ]

        def sub_punctuation_between_lithuanian_double_quotes(self, txt):
            return re.sub(
                self.BETWEEN_LITHUANIAN_DOUBLE_QUOTES_REGEX, replace_punctuation, txt
            )

        def sub_punctuation_in_dialog(self, txt):
            return Text(txt).apply(*self.DialogRules.All)

        def sub_punctuation_between_quotes_and_parens(self, txt):
            txt = super().sub_punctuation_between_quotes_and_parens(txt)
            txt = self.sub_punctuation_between_lithuanian_double_quotes(txt)
            txt = self.sub_punctuation_in_dialog(txt)
            return txt
