'''
Created on 2015. 12. 2.

@author: USER
'''
def observed(sent, network):
    """
    >>> network = {1:{2, 5}, 2:{1, 5, 3}, 3:{2, 4}, 4:{3, 5, 6}, 5:{1, 2, 4}, 6:{4}}
    >>> observed({1, 2}, network)
    {3, 5}
    >>> observed({3, 4}, network)
    {2, 5, 6}
    """
    # find all stations where the smoke signals set are observed
    observed = set()
    for station in sent:
        observed.update(network[station])
    # return all stations where the smoke signals set are observed and that do
    # not send smoke signals themselves
    return observed - sent

def distribution(station, network):
    """
    >>> network = {1:{2, 5}, 2:{1, 5, 3}, 3:{2, 4}, 4:{3, 5, 6}, 5:{1, 2, 4}, 6:{4}}
    >>> distribution(1, network)
    3
    >>> distribution(4, network)
    2
    """
    # at time zero a smoke signal is sent from the given station
    steps, received = 0, {station}
    # all stations that have received a smoke signal, start spreading the signal
    # themselves until all stations have received a smoke signal
    while len(received) != len(network):
        # all stations that have received a smoke signal, start spreading the
        # signal across the network in the next time step
        steps += 1
        # add all stations that have received a smoke signal to the set that
        # contains all stations that have received a smoke signal
        received.update(observed(received, network))
    # return the number of time steps needed to spread the smoke signals across
    # the entire network
    return steps