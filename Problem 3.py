import Problem_1 as Cls
import scr.SamplePathClass as SamplePathSupport
import scr.FigureSupport as Fig

LOSS_PROB = 0.607       # annual probability of loss for a player - which is a win for a casino
CAS_POP_SIZE = 1000     # the number of games for a casino
PLA_POP_SIZE = 10       # the number of games for a player
TIME_STEPS = 100        # simulation length
ALPHA = 0.05            # significance level

# create a cohort of games
myCohort = Cls.SetOfGames(n_games=PLA_POP_SIZE, get_probability_loss=LOSS_PROB)
myCasino = Cls.SetOfGames(n_games=CAS_POP_SIZE, get_probability_loss=LOSS_PROB)

# simulate the cohort
cohortOutcome = myCohort.simulate(TIME_STEPS)
casinoOutcome = myCasino.simulate(TIME_STEPS)


# print 95% confidence interval of average survival time
print('95% confidence interval of player', cohortOutcome.get_CI_survival_times(ALPHA))
print('95% confidence interval of casino owner', casinoOutcome.get_CI_survival_times(ALPHA))


