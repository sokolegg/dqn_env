from gym.envs.registration import register

register(
    id='dqn_env-v0',
    entry_point='dqn_env.envs:DQNEnv'
)
