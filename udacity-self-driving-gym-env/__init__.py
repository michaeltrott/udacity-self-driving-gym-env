from gym.envs.registration import register

register(
    id='udacity-gym-env-v0',
    entry_point='gym_udacity.envs:UdacityEnv',
)
