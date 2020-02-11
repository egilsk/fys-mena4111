if [ -n "$PS1" ]; then PS1='\h:\W\$ '; fi

# aliases...

alias cpu="grep 'Total CPU time'"
alias e="emacs -geometry 100x60+210+110 -font fixed >& /dev/null &"
alias endir='toten */OUTCAR'
alias f="finger"
alias h="history"
alias ll="ls -al | more"
alias lt="ls -lt | more"
alias mfs="maxforceselective"
alias qlogin="qlogin --account=ln0003k"
alias rm="rm -i"
alias rm~="rm -f *~"
alias st='squeue -u $USER -o "%.9i %.8j %.10M %.6D %.6C %l %R"'
alias sub="sbatch jobfile"
alias vasp_clean="find . \( -name WAVECAR -o -name 'CHG' \) -exec rm {} \;"
alias vesta="VESTA"
alias xv="display"
#
umask 027

export HISTCONTROL=ignoreboth

# Modules loaded by default:

module load Anaconda3
module load gnuplot
module load vesta
module load imagemagick
export PATH=/usit/abel/u1/olem/fm4111/bin:$PATH
export PYTHONPATH=/usit/abel/u1/olem/fm4111/python:$PYTHONPATH

