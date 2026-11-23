# EdgeEnergy

![Energy transfer, report selection and event sensing in a wireless sensor network](edgeenergy-overview.svg)

A sensor can miss an event while a neighbour still has energy to spare. Can the energy reach the right node, does the scheduler know enough to act, and will the sensor be awake when the event arrives? These questions connect the three studies in Guoqing Lu’s PhD project, *EdgeEnergy: Ambient Energy Harvesting and Energy Cooperative Wireless Sensor Network*, Department of Computing and Mathematics, South East Technological University (SETU), Waterford.

[Download the research package](EdgeEnergy_Research_GitHub.zip) · [Run an example](#run-an-example) · [Chapter and output index](REPRODUCTION_COVERAGE.md)

| Decision | Method | What changed in the experiments |
|---|---|---|
| How many donors should supply one receiver? | Dynamic-K adapts the limit on concurrent donors. | Across five schedulers in the 25-node simulation, mean energy dispersion fell by **64.4%** relative to one donor; network-accounted transfer loss rose by **43.5%**. |
| Which energy reports are worth sending? | Decision-Aware Information–Energy Scheduling with Safeguarded Payer Reserves (DA-IES-S) selects reports that could change a feasible transfer and checks the payer’s reserve. | Under combined stress in the multihop corridor, reserve events fell from **27.69% to 6.68%** versus urgency-times-age scheduling. Both exceeded the 3% target. |
| Which sensors should wake or be revisited? | Sentinel-assisted sampling detects local changes; DF-ReAlert revisits sensors as an anomaly spreads. | On the 54-node record, anomaly-window sampling rose from **43.9% to 93.3%** relative to sparse Kalman sampling. In the second moving-front window, selective revisits required fewer routed command receptions than a fixed two-hop response but caught fewer arrivals. |

## Run an example

Use CPython 3.12 on 64-bit Linux. The simulations run on a CPU and need no network access after installation. The launcher reads the ZIP directly. To explore the source and run full study sweeps, download and extract the [research package](EdgeEnergy_Research_GitHub.zip).

```sh
git clone https://github.com/Guoqing0110/EdgeEnergy.git
cd EdgeEnergy
python3.12 -m venv ../edgeenergy-env
. ../edgeenergy-env/bin/activate
python -m pip install -r requirements.txt
python -B reproduce.py --only stage-ii --output ../edgeenergy-front
```

Open `../edgeenergy-front/stage-ii/runs.csv`. For DF-ReAlert on seed 422, front recall is **0.5163934**, with **809 routed command receptions** and **366.594 J** of modelled energy (the CSV stores millijoules). To run all three study examples, use `python -B reproduce.py --output ../edgeenergy-results`. Choose a new output directory for each run.

The ten-node testbed recorded radio traffic and acknowledgements; the host modelled energy transfers and costs. The hardware examples analyse or replay these records. For a short illustration of the donor decision without installing the simulator, see the [Dynamic-K worked example](https://github.com/Guoqing0110/dynamic-k-demo).

[License notice](LICENSE) · [Software and data attribution](LICENSE_SCOPE.md) · [MIT terms](MIT.txt)

**SHA-256 of the downloadable ZIP:** `575ccd234f99214f5de8f399c674bdd45ba8ec21267e1d024f707f68a65f81da`.
