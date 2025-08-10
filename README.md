# Custom IPv4 Router & Firewall

A Mininet-style Layer‑3 router and firewall policy engine. Includes unit tests for ICMP filtering, subnet isolation, and anti‑spoofing rules. Mininet topology file is included as a placeholder for future integration tests.

## Features
- 20-host segmented network (topology placeholder)
- 10+ rules including ICMP flood block and anti‑spoofing
- Unit tests for critical scenarios (Pytest)
- Clean, extensible policy engine

## Tech Stack
**Python**, **Pytest**, (Mininet/POX integration optional)

## Quickstart
```bash
git clone https://github.com/rami-saad/ipv4-router-firewall.git
cd ipv4-router-firewall
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

## Roadmap
- Ryu/SDN port
- Prometheus metrics export
- Full Mininet system tests
