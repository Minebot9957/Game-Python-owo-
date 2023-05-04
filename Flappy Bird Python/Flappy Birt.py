import pygame, sys , random

def draw_floor():
	screen.blit(fl,(fl_x_pos,600))
	screen.blit(fl,(fl_x_pos+432,600))	
def create_pipe():
	random_pipe_pos = random.choice(pipe_height)
	bottom_pipe = pipe_suface.get_rect(midtop = (500,random_pipe_pos))
	top_pipe = pipe_suface.get_rect(midtop = (500,random_pipe_pos-750))
	return bottom_pipe, top_pipe
def move_pipe(pipes):
	for pipe in pipes :
		pipe.centerx -= 4
	return pipes
def draw_pipe(pipes):
	for pipe in pipes:
		if pipe.bottom >= 550 :
			screen.blit(pipe_suface,pipe)
		else :
			flip_pipe = pygame.transform.flip(pipe_suface,False,True)			
			screen.blit(flip_pipe,pipe)
def check_collision(pipes):
	for pipe in pipes:
		if bird_rect.colliderect(pipe):
			hit_sound.play()
			return False
	if bird_rect.top <= -75 or bird_rect.bottom >= 650:
			die_sound.play()
			return False
	return True				
def rotate_bird(bird1):
	new_bird = pygame.transform.rotozoom(bird1,-bird_movement*3,1)
	return new_bird	
def bird_animation():
	new_bird = bird_list[bird_index]
	new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
	return new_bird,new_bird_rect	
def score_display(game_state):
	if game_state == 'main game':
		score_suface = game_font.render(str(int(score)),True,(255,255,255))
		score_rect = score_suface.get_rect(center = (216,100))
		screen.blit(score_suface,score_rect)
	if game_state == 'game_over':
		score_suface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
		score_rect = score_suface.get_rect(center = (216,50))
		screen.blit(score_suface,score_rect)

		high_score_suface = game_font.render(f'High Score: {int(high_score)}',True,(255,255,255))
		high_score_rect = high_score_suface.get_rect(center = (216,565))
		screen.blit(high_score_suface,high_score_rect)

def update_score(score,high_score):
	if score > high_score:
		high_score = score
	return high_score
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
screen = pygame.display.set_mode((432,768))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
game_font = pygame.font.Font('C:/Users/CuongNguyenPC/Documents/Code/Flappy Bird Python/FileGame/FileGame/04B_19.TTF', 40)

gravity = 0.5
bird_movement = 0
game_active = True
score = 0
high_score = 0 

bg = pygame.image.load('C:/Users/CuongNguyenPC/Documents/Code/Flappy Bird Python/FileGame/FileGame/assets/background-night.png').convert()
bg = pygame.transform.scale2x(bg)
bg_x_pos = 0

fl = pygame.image.load('C:/Users/CuongNguyenPC/Documents/Code/Flappy Bird Python/FileGame/FileGame/assets/floor.png').convert()
fl = pygame.transform.scale2x(fl)
fl_x_pos = 0
#taochim
bird_down = pygame.image.load('C:/Users/CuongNguyenPC/Documents/Code/Flappy Bird Python/FileGame/FileGame/assets/redbird-downflap.png').convert_alpha()
bird_down = pygame.transform.scale2x(bird_down)
bird_mid = pygame.image.load('C:/Users/CuongNguyenPC/Documents/Code/Flappy Bird Python/FileGame/FileGame/assets/redbird-midflap.png').convert_alpha()
bird_mid = pygame.transform.scale2x(bird_mid)
bird_up = pygame.image.load('C:/Users/CuongNguyenPC/Documents/Code/Flappy Bird Python/FileGame/FileGame/assets/redbird-upflap.png').convert_alpha()
bird_up = pygame.transform.scale2x(bird_up)
bird_list = [bird_down,bird_mid,bird_up]
bird_index = 0
bird = bird_list[bird_index]
bird_rect = bird.get_rect(center = (100,384))

bird_flap = pygame.USEREVENT + 1
pygame.time.set_timer(bird_flap,200)

pipe_suface = pygame.image.load('C:/Users/CuongNguyenPC/Documents/Code/Flappy Bird Python/FileGame/FileGame/assets/pipe-green.png').convert() 
pipe_suface = pygame.transform.scale2x(pipe_suface)
pipe_list = []

spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)
pipe_height = [300,400,550,200,100]
#tao man hinh ket thuc
game_over_suface = pygame.image.load('C:/Users/CuongNguyenPC/Documents/Code/Flappy Bird Python/FileGame/FileGame/assets/message.png').convert_alpha()
game_over_suface = pygame.transform.scale2x(game_over_suface)
game_over_rect = game_over_suface.get_rect(center = (216,330))
#chen am thanh
hit_sound = pygame.mixer.Sound('C:/Users/CuongNguyenPC/Documents/Code/Flappy Bird Python/FileGame/FileGame/sound/sfx_hit.wav')
swood_sound = pygame.mixer.Sound('C:/Users/CuongNguyenPC/Documents/Code/Flappy Bird Python/FileGame/FileGame/sound/sfx_swooshing.wav')
die_sound = pygame.mixer.Sound('C:/Users/CuongNguyenPC/Documents/Code/Flappy Bird Python/FileGame/FileGame/sound/sfx_die.wav')
score_sound = pygame.mixer.Sound('C:/Users/CuongNguyenPC/Documents/Code/Flappy Bird Python/FileGame/FileGame/sound/sfx_point.wav')
flap_sound = pygame.mixer.Sound('C:/Users/CuongNguyenPC/Documents/Code/Flappy Bird Python/FileGame/FileGame/sound/sfx_wing.wav')
point_sound = 100 
#while loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and game_active:
				bird_movement = 0
				bird_movement =-11
				flap_sound.play()
			if event.key == pygame.K_SPACE and game_active==False:
				game_active = True
				pipe_list.clear()
				bird_rect.center = (100,348)
				bird_movement = 0
				score = 0 

		if event.type == spawnpipe:
		    pipe_list.extend(create_pipe())
		if event.type == bird_flap:
			if bird_index < 2 :
				bird_index += 1
			else :
				bird_index =0
			bird, bird_rect = bird_animation()		    

	screen.blit(bg,(0,0))
	if game_active:
		bird_movement += gravity
		rotated_bird = rotate_bird(bird)
		bird_rect.centery += bird_movement		
		screen.blit(rotated_bird,bird_rect)
		game_active = check_collision(pipe_list)
	
		pipe_list = move_pipe(pipe_list)
		draw_pipe(pipe_list)
		score += 0.01
		score_display('main game')
		point_sound -= 1
		if point_sound <= 0:
			score_sound.play()
			point_sound = 100


	else :
		screen.blit(game_over_suface,game_over_rect)
		high_score = update_score(score,high_score)
		score_display('game_over') 	
	
	fl_x_pos -= 1
	draw_floor()
	if fl_x_pos <= -432:
	 	fl_x_pos =0

	pygame.display.update()
	clock.tick(60)		
	