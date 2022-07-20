from gym.envs.registration import register

register(
    id='walk1D-v0',
    entry_point='gym_foo.envs:FooEnv',
)
