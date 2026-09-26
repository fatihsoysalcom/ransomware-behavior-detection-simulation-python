# Ransomware Behavior Detection Simulation Python

This example simulates a ransomware attack by creating dummy files, 'corrupting' their content, and renaming them with a suspicious extension. It then demonstrates a basic detection mechanism that identifies ransomware-like activity by counting files with the new, unknown extension. This illustrates the behavioral patterns that advanced monitoring tools like ETW and eBPF would detect at a lower level.

## Language

`python`

## How to Run

Save the code as `ransomware_sim.py`. Run it from your terminal: `python ransomware_sim.py`.

## Original Article

This example accompanies the Turkish article: [ETW ve eBPF ile Windows ve Linux Ortamlarında Fidye Yazılımı Tespiti: Derinlemesine Bir Bakış](https://fatihsoysal.com/blog/etw-ve-ebpf-ile-windows-ve-linux-ortamlarinda-fidye-yazilimi-tespiti-derinlemesine-bir-bakis/).

## License

MIT — see [LICENSE](LICENSE).
