from law_process import LawProcess
from legislative_initiative import LegislativeInitiative
from committee_consideration import CommitteeConsideration
from parliament_discussion import ParliamentDiscussion
from voting import Voting
from speaker_signature import SpeakerSignature
from president_signature import PresidentSignature
from publication import Publication


if __name__ == "__main__":
    print("Створення законодавчої ініціативи закону про ...")
    law = LawProcess("Закон про ...")
    law.handle(CommitteeConsideration)
    law.handle(ParliamentDiscussion)
    law.handle(Voting)
    law.handle(SpeakerSignature)
    law.handle(PresidentSignature)
    law.handle(Publication)
    # Наступні переходи, що не входять у логіку, будуть виводити повідомлення про неможливість зміни стану.
    law.handle(LegislativeInitiative)
    law.handle(ParliamentDiscussion)
