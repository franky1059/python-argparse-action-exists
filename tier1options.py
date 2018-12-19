



def initialize_args(parser_obj = None):
	parser_obj.add_argument("-t1o1", "--tier1_option1",
						dest="tier1_option1",
						default="",
						type=str,
						help="Option execution for this tier")
						
	parser_obj.add_argument("-t1o2", "--tier1_option2",
						dest="tier1_option2",
						default="",
						type=str,
						help="Option execution for this tier")