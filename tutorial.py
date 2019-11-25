import gym
import random

EPISODES  = 5

def main():
	env = gym.make('BankHeist-v0')
	print(env.observation_space)
	print(env.action_space)
	episode_reward = 0
	for i in range(EPISODES):
		env.reset()
		episode_reward = 0
		
		while True:
			action = env.action_space.sample()
			state, reward, done, info = env.step(action)
			episode_reward += reward
			if done:
				print('Reward: %s' % episode_reward)
				break

main()
