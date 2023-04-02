from utils.arguments import Arguments


if __name__ == '__main__':

    argument = Arguments()
    print('command line')
    print(argument.getCommandLine())
    print('')

    task_folder = argument.getArgument('task_folder', './task_folder/')
    output_folder = argument.getArgument('output_folder', './output_folder/')

