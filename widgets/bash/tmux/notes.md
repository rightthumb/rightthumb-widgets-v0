# tmux

[chat](https://chat.openai.com/c/60aa33fe-fcf2-437c-979b-87b56a0e3831)


## navigation

`ctrl+b   arrows`

## detach from session

`ctrl+b   d`

## commands

~~~sh

tmux list-sessions

# reattach session
tmux attach-session -t session-name

# kill session
tmux kill-session -t session-name

# kill all sessions
tmux list-sessions | grep -v attached | cut -d: -f1 | xargs -I {} tmux kill-session -t {}
~~~

### script example

~~~sh
# new session
tmux new-session -d -s MySession
# 2 horizontal panes
tmux split-window -h
#split all  vertically
tmux select-pane -t 0
tmux split-window -v
tmux select-pane -t 2
tmux split-window -v
# attach session
tmux attach-session -t MySession
~~~
