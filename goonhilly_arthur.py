from mcpi import minecraft
from mcpi import block
from time import sleep
from arthur_blocks import dish_block_positions

mc = minecraft.Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.setBlock(x,y-1,z,block.LAPIS_LAZULI_BLOCK.id)

read_block_data = 0

# Build the base in brick
mc.setBlocks(x-10, y, z-8, x+8, y+20, z-25, block.AIR.id)
mc.setBlocks(x-9, y-5, z-8, x+6, y, z-24, block.BRICK_BLOCK.id)


# Build the dish
while read_block_data < len(dish_block_positions):
    x_position = dish_block_positions[read_block_data] # read first position
    read_block_data += 1
    y_position = dish_block_positions[read_block_data] # read second position
    read_block_data += 1
    z_position = dish_block_positions[read_block_data] # read third position
    read_block_data += 1
    block = dish_block_positions[read_block_data] # read block identity
    read_block_data += 1
    mc.setBlock(x+x_position, y+y_position, z+z_position, block) # place the block in position
    #sleep(0.1)
