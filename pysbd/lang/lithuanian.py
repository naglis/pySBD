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
            "avd",  # asmenvardis
            "biol",
            "b. k",
            "bkl",
            "bot",
            "bt",
            "buv",
            "chem",
            "d",  # duktė; diena
            "dail",
            "dek",
            "dėst",
            "dir",
            "dirig",
            "doc",
            "dr",
            "drp",  # durpynas
            "dš",
            "e",  # elektroninis
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
            "G",  # Galininkas
            "gen",
            "geol",
            "gerb",
            "gim",  # gyvenvietė
            "gv",
            "gyd",
            "įl",
            "Įn",  # Įnagininkas
            "insp",
            "inž",
            "ir pan",
            "ir t. t",
            "istor",
            "J. E",  # Jo Ekscelencija
            "J. Em",  # Jo Eminencija
            "k",  # kaimas
            "K",  # Kilmininkas
            "k. a",  # kaip antai
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
            "m. e",  # mūsų eros
            "med",
            "mėn",
            "mgr",
            "mjr",
            "mln",
            "mlrd",
            "m. m",  # mokslo metai
            "mok",
            "mokyt",
            "mot",
            "mst",
            "mstl",
            "N",  # Naudininkas
            "nkt",  # nekaitomas
            "ntk",
            "p",  # ponas, ponia, panelė; puslapis; punktas
            "pav",
            "pavad",
            "p. d",
            "pirm",
            "pl",
            "plg",
            "plk",
            "p. m. e",  # prieš mūsų erą
            "pr",
            "pranc",
            "pr. Kr",
            "prof",
            "prok",
            "prot",  # protokolas
            "psl",
            "pss",  # pusiasalis
            "pšt",
            "pvz",
            "r",  # rajonas
            "red",
            "rš",
            "s",  # sūnus, sąskaita
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
            "sr",  # sritis
            "str",
            "stud",
            "t",  # tomas
            "techn",
            "tel",
            "teol",
            "tir",
            "t. p",
            "tūkst",
            "t. y",
            "up",
            "upl",
            "V",  # Vardininkas
            "vad",
            "ved",
            "vet",
            "virš",
            "vlsč",
            "vnt",
            "vs",
            "Vt",  # Vietininkas
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

    class EllipsisRules(Standard.EllipsisRules):
        ExclamationTwoRule = Rule(r"\!\.\.", "&ᓴ&∯.")
        # https://rubular.com/r/zrmWh8sRQ4R8Ay
        HorizontalEllipsis = Rule(r"…(?=\s+[A-Ž])", "☍☍.")

        All = Standard.EllipsisRules.All + [ExclamationTwoRule, HorizontalEllipsis]

    class ReinsertEllipsisRules(Standard.ReinsertEllipsisRules):
        HorizontalEllipsis = Rule(r"☍☍.", "…")

        All = Standard.ReinsertEllipsisRules.All + [HorizontalEllipsis]
