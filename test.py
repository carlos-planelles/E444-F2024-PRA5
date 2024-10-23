import time
import requests

# URL = "http://planelle.us-east-2.elasticbeanstalk.com/"
URL = "http://127.0.0.1:5000/"

TEXT_DOCS_FAKE = (
    "A recent study conducted by the University of Nutrition found that eating three bars of chocolate a day results in immediate weight loss. The researchers claim that chocolate boosts metabolism so effectively that most participants shed five pounds within a week without changing their diet. Despite skepticism from the medical community, the findings have sparked a surge in chocolate sales nationwide.",
    "A team of international scientists has announced the discovery of a massive, hidden city buried deep under Antarctica's ice sheet. The city, estimated to be over 10,000 years old, contains structures and artifacts that suggest an advanced civilization once thrived there. The discovery has reignited conspiracy theories about ancient technology and secret government knowledge of extraterrestrial life.",
)

TEXT_DOCS_REAL = (
    "A report by KPMG indicates that 87 percent of Canadian business leaders worry the U.S. Election could harm the Canadian economy due to protectionist policies. The survey reveals that 85 percent of Canadian business leaders are changing strategies in response to potential U.S. Leadership shifts. Business concerns are mostly from larger companies, especially in manufacturing and automotive sectors, impacted by U.S. Economic ties.",
    'Liberal MP Sean Casey confirmed he signed a letter calling on Prime Minister Justin Trudeau to resign, stating it would be in the best interests of the country. Casey believes Canadians are distracted by Trudeau, affecting the government\'s effectiveness, saying, "People have tuned him out." Reports suggest a group of Liberal MPs plans to confront Trudeau about poor poll numbers at the upcoming caucus meeting.',
)


def test_correctness():
    data = {"documents": TEXT_DOCS_FAKE + TEXT_DOCS_REAL}
    r = requests.post(url=URL + "is-fake", json=data)

    assert r.json() == {"results": ["FAKE", "FAKE", "REAL", "REAL"]}


def test_latency():
    data = [
        {"documents": TEXT_DOCS_FAKE[0] + TEXT_DOCS_REAL[0]},
        {"documents": TEXT_DOCS_FAKE[1] + TEXT_DOCS_REAL[0]},
        {"documents": TEXT_DOCS_FAKE[0] + TEXT_DOCS_REAL[1]},
        {"documents": TEXT_DOCS_FAKE[1] + TEXT_DOCS_REAL[1]},
    ]
    timestamps = ""
    for i in range(100):
        before = time.time()
        requests.post(url=URL + "is-fake", json=data[i % 4])
        after = time.time()
        timestamps += f"{before},{after},{after-before}\n"

    with open("timestamps.csv", "w") as f:
        f.write(timestamps)


if __name__ == "__main__":
    test_correctness()
    test_latency()
