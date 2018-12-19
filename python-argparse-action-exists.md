

Using argparse to Tier Software Product Offerings
--------------------------------------
#### The argparse Module
The argparse module came on the scene in release 3.2 and it's been a great tool for command line (cli) argument parsing, replacing modules like getopt with a more user friendly interface and better features. ETL and analysis workflows are almost always done via the shell or command-line in one way or another so robust command line parsing is a must for professional developer. 

#### Cli Arguments In An Enterprise Code-base
Creating an ArgumentParser object and adding action arguments is easy as pie... 
<pre>
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
</pre>
... but what happens in a scenario where a particular action needs to be tested to not only be certain value, but to test the very existence of the action in the ArgumentParser itself? This scenario can occur if, for example, we have a large code-base that dynamically loads certain functional components based on a configuration or environmental set of circumstances.
<pre>
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
</pre>
A particular use-case may be if we build and sell a traditional software product, say an ETL tool similar to Talend, that can be shipped for use by different end-users or clients that have paid or not have paid for the use of particular functional packages in the tool. This is a common business model especially in the enterprise software world with ETL and Analysis products like SSIS, SAS, etc. <br/>
Architecturally this may mean that the software code-base will require different cli arguments depending on which functional components are enabled, but it's important that the main cli entry-point uses the same block of code to initiate execution requests. The reason for this is so that we don't duplicate functionality in different parts of the code-base which makes code more prone to regressive bugs and increases maintenance and time costs as the product is developed and maintained. <br/>
So what does this all have to do with detecting defined actions in an ArgumentParser object? Because in this scenario cli arguments would be dynamically defined based on the enabled product functionality components the customer has paid for. During run-time other components may need to test whether an associated cli argument has been passed in, but there's no guarantee that it will be there.. and we all know what happens when code tries to invoke a non-existent member or function... hint hint.. NULL errors.

#### What Actions are Defined
The ArgumentParser object contains an iterable member of action items called "_actions". We can loop through each action item and test to see if the "dest" member matches the cli argument we're looking for. 
<pre>
current_arg_actions = parser_obj._actions
for action_item in current_arg_actions:
	if (action_item.dest == action_dest):
		action_exists = True
</pre>
There may be another convenience function in the argparse model that accomplishes this goal, but at least this way we can see what's going on under the hood - which always turns out to be useful knowledge one way or the other. 





Code
--------------------------------------	
- [python-argparse-action-exists (GitHub)](https://github.com/franky1059/python-argparse-action-exists)



Links
--------------------------------------
- [Creating a parser (python3 docs)](https://docs.python.org/3/library/argparse.html#creating-a-parser)
- [argparse tutorial (python3 docs)](https://docs.python.org/3/howto/argparse.html)
- [argparse api ref (python3 docs)](https://docs.python.org/3/library/argparse.html)
- [How to parse command line arguments in Python (dev blog)](https://martin-thoma.com/how-to-parse-command-line-arguments-in-python/)
- [skipping unkown args](https://stackoverflow.com/questions/12818146/python-argparse-ignore-unrecognised-arguments)
- [argparse examples](https://sites.google.com/site/kittipat/programming-with-python/pythontakingargumentsfromcommandlinewithargparse)



