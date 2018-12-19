
import inspect
import pprint
import os, sys
import configparser




config_parser = None


def debug_info():
	line_no = inspect.currentframe().f_back.f_lineno
	fcn_name = inspect.currentframe().f_back.f_code.co_name
	print("Line: " + str(line_no))
	print("Fcn: " + str(fcn_name))

def debug_pprint(var):
	pp = pprint.PrettyPrinter(indent=4)
	pp.depth = 6
	pp.pprint(var)
		
		


	
def argparse_action_exists(parser_obj = None, action_dest = ''):
	action_exists = False

	current_arg_actions = parser_obj._actions
	for action_item in current_arg_actions:
		if (action_item.dest == action_dest):
			action_exists = True

	return action_exists


	
def initialize_arg_parser():
	from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
	parser = ArgumentParser(description=__doc__,
							formatter_class=ArgumentDefaultsHelpFormatter)	
						
	enabled_mods = config_parser.get("app", 'enabled_mods')
	enabled_mods_list = enabled_mods.split(',')
	
	if 'tier1' in enabled_mods_list:
		import tier1options
		tier1options.initialize_args(parser_obj = parser)
		
	if 'tier2' in enabled_mods_list:
		import tier2options
		tier2options.initialize_args(parser_obj = parser)
			
	
	return parser
	
	
	
	
if __name__ == '__main__':
	config_parser = configparser.ConfigParser()
	config_parser.readfp(open('config.ini'))
	
	parser = initialize_arg_parser()
	cli_args, unknown = parser.parse_known_args(args=sys.argv[1:])
	

	tier1_option1_action_exists = argparse_action_exists(parser_obj = parser, action_dest = 'tier1_option1')

	print('__file__: ' + __file__ + ' ')
	debug_info()
	print('tier1_option1_action_exists: ')
	debug_pprint(tier1_option1_action_exists)
	
	
	tier2_option1_action_exists = argparse_action_exists(parser_obj = parser, action_dest = 'tier2_option1')

	print('__file__: ' + __file__ + ' ')
	debug_info()
	print('tier2_option1_action_exists: ')
	debug_pprint(tier2_option1_action_exists)
	
	
	
	
	