import unittest
from cobra import CobraMonitor

class TestCobra(unittest.TestCase):
    def test_low_divergence_low_risk(self):
        m = CobraMonitor()
        out = m.update(0.05,0.0,0.5,0.5,0.0)
        self.assertLess(out["risk_score"],0.1)

    def test_persistence_accumulates(self):
        m = CobraMonitor()
        a = m.update(0.5,0.0)
        b = m.update(0.5,0.0)
        self.assertGreater(b["persistent_divergence"], a["persistent_divergence"])

    def test_proxy_divergence_detected(self):
        m = CobraMonitor()
        m.update(0.1,0.0,0.5,0.5)
        out = m.update(0.1,0.0,0.8,0.4)
        self.assertGreater(out["proxy_divergence"],0.0)

if __name__ == "__main__":
    unittest.main()
