# Using the software and data

Guoqing Lu is the thesis author and an author of the research implementations. He authorises the use of his own research-code contributions to reproduce the experiments. Where he holds the right to license those contributions, he offers them under the [MIT License](MIT.txt). MIT permits uses beyond scientific reproduction; copies or substantial portions must retain its notices. This statement does not identify him as sole author or owner of every module, and does not assign the authorship of new packaging tools to him.

**New reproduction tools and documentation — MIT.** The following files were prepared for this distribution and are licensed under [MIT](MIT.txt), with the notice “Contributors to the thesis reproduction tools”:

- Launcher and installation files: `reproduce.py`, `requirements.txt`.
- User documentation: `README.md`, `docs/USER_GUIDE.md`, `docs/QUICKSTART.md`. The repository overview illustration is `docs/assets/edgeenergy-overview.svg`.
- Offline HIL verification and projection: `hil/check_hil.py`, `hil/dynamic-k/verify.py`, `hil/dynamic-k/project_archive.py`, `hil/da-ies-s/verify.py`.
- Distribution metadata: `.gitignore`, `.gitattributes`, `CHECKSUMS.sha256`.

These tools read existing algorithms and research records. The MIT license applies to the listed files, not to an input, table or historical engine just because a listed file loads, describes or identifies it. Use of the collective notice does not assign individual authorship of the original algorithms.

| Material | Origin and terms |
|---|---|
| Dynamic-K: `experiments/dynamic-k/source/` | Research software for the study by Guoqing Lu and Bernard Butler. The source archive has no accompanying license that covers the complete tree. The author's grant above applies only to contributions he can license. |
| DA-IES-S: `experiments/da-ies-s/engines/v1/` and `v2/` | These are two separate research snapshots used for Chapter 5. The author's grant applies to his eligible code contributions. No license covering all files in either snapshot was found. The configurations, seed mappings and output tables are study records and are outside the MIT grant. |
| Sentinel sensing: `experiments/adaptive-sampling-monitoring/task10/source/`, `experiments/adaptive-sampling-monitoring/source/` | Simulation and host-side replay code from the study by Guoqing Lu, Yixuan Sun, Yiwen Jiang and Bernard Butler. No license covering these complete source trees was identified. The author's own eligible code contributions are covered as stated above. |
| Other experiment adapters and documentation | Adapters, table checks or documentation outside the explicit MIT list above do not acquire that license solely through use by the root launcher. Preserve the original terms of any incorporated code. |
| Reference values and HIL records | Result tables, reference outputs, event projections, hardware-session inputs and acquisition descriptions, including data under `hil/`, are project research materials. No general redistribution license is supplied for these materials. The MIT software license does not cover them. |
| Intel Lab Data | The temperature window and sensor-position table under `experiments/adaptive-sampling-monitoring/task10/input/` use Intel Berkeley Research Lab data. The directed communication-edge table represents the realised network used by Task 10; credit the original data as well as the experiment when using these inputs. See below. |
| Python and other dependencies | Python packages installed in the user's environment retain their respective upstream terms. They are not licensed by this repository. |

**Intel Lab Data acknowledgement.** The dataset was collected at Intel Berkeley Research Lab. We thank Peter Bodik, Wei Hong, Carlos Guestrin, Sam Madden, Mark Paskin and Romain Thibaux. The [dataset's source page](https://db.csail.mit.edu/labdata/labdata.html) allows the data to be used or reproduced in any format or venue. The collectors ask to be acknowledged in published work and do not warrant data quality or accuracy. The aligned window, node selection and realised graph are experiment-specific representations. MIT's software license is not the license for Intel Lab Data.

**When reusing files.** Preserve attribution and original notices. Scientific authorship, the right to release code and the right to redistribute research records are separate. For a file with no applicable public license identified above, obtain permission from the relevant rights holder before redistribution. A citation identifies the source; it does not grant that permission.

The [public Dynamic-K example](https://github.com/Guoqing0110/dynamic-k-demo) is a separate distribution. Consult its own license and notices when using it.

**Chapter 6 Stage II.** In `experiments/adaptive-sampling-monitoring/stage-ii/`, the new run, input-preparation and verification scripts in `scripts/` and their user documentation are reproduction tools under the contributor MIT notice. The research modules in `src/` retain their original authorship and terms; Guoqing Lu's grant above covers only contributions he is entitled to license. Registered experiment records, result tables and testbed records are not covered by the software grant. The two-day input and node files are credited to the Intel Lab data collection under the dataset terms above. In `experiments/thesis-tables/`, the new verification program and its guide use the contributor MIT notice; the underlying research data retain their own terms.
