#
# context sample
#

import sys
sys.path.append("..")

import izpyc
import izpyc.constraint as C
from izpyc import Int

with izpyc.space():

    # create variable
    a = Int(0, 9)
    
    with izpyc.save_context() as context:
        # a = {0..5}
        a <= 5
        print("001: a = {}".format(a))
    
        with izpyc.save_context() as context:
            a >= 3
            # a = {3..5}
            print("002: a = {}".format(a))

            # lower bound will not be restored at end of scope of "with"
            context.forget_save();

        # a = {3..5}
        print("003: a = {}".format(a))

    # lower bound has been restored.
    # upper bound has been restored.
    # a = {0..9}
    print("004; a = {}".format(a))
