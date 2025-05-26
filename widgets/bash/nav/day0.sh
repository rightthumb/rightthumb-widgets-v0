#!/bin/bash
source $HOME/.bashrc
$m back   > /dev/null 2>&1
echo ''    >> $HOME/.bashrc.once.print
echo last fo: b.back >> $HOME/.bashrc.once.print
$bb back   >> $HOME/.bashrc.once.print
echo ''    >> $HOME/.bashrc.once.print
echo 1w <, d: 7, h: 0, m: 0, s: 4   >> $HOME/.bashrc.once.print
echo /home/scott/.rt/profile/daily/2022/28/07-14/  >> $HOME/.bashrc.once.print
echo ''    >> $HOME/.bashrc.once.print
sed -i 's/^/        /' $HOME/.bashrc.once.print
if [ ! -f /home/scott/.rt/profile/daily/2022/28/07-14//notes.md ]
then
touch /home/scott/.rt/profile/daily/2022/28/07-14//notes.md
fi
$cdf /home/scott/.rt/profile/daily/2022/28/07-14//notes.md