ACTOR_HIDDENS = [128, 128]
CRITIC_HIDDENS = [128, 128]
VALUE_HIDDENS = [128, 128]

ACTOR_LR = 3 * 1e-3
CRITIC_LR = 3 * 1e-3
VALUE_LR = 3 * 1e-3

REG_FACTOR = 1e-3
GAMMA = 0.99
TAU = 1e-2
BATCH_SIZE = 16

BUFFER_SIZE = 10 ** 6

FINAL_STEP = 10 ** 6

MODEL_SAVE_INTERVAL = 10 ** 5
