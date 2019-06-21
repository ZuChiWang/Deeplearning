import numpy as np
import gym

GAME = 'FrozenLake-v0'
env = gym.make(GAME)
print(env)
MAX_STEPS = 2000
EPSILON=0.8
GAMMA=0.8
ALPHA=0.01
q_table=np.zeros([16,4],dtype=np.float32)

def action_choise(obervation):
    if np.random.uniform()<EPSILON:
        action=np.argmax(q_table[obervation])
    else:
        action=env.action_space.sample()
    return action

def learn(state,action,reward,obervation):
    q_table[state][action]+=ALPHA*(reward+GAMMA*max(q_table[obervation])-q_table[state,action])


SCORE=0
for exp in range(10000):
    obervation=env.reset()
    EPSILON+=0.001
    for i in range(MAX_STEPS):
        # env.render()
        action=action_choise(obervation)          #动作选择
        obervation_,reward,done,info=env.step(action)    #学习
        SCORE+=reward
        if reward==0:
            if done:
                reward=-1
            else:
                reward=-0.001
        learn(obervation,action,reward,obervation_)
        obervation=obervation_
        if done:
            break
    print('esp,score (%d,%d)'%(exp,SCORE))
print('score is %d'%SCORE)