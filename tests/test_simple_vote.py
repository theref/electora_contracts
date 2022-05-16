import ape


def test_add_candidate(owner, candidate, project):
    simple_vote = owner.deploy(project.SimpleVote)
    simple_vote.add_candidate(candidate, "New Candidate", sender=owner)
    assert simple_vote.candidates(candidate).name == "New Candidate"
    assert simple_vote.candidates(candidate).vote_count == 0


def test_register_voter(owner, voter, random, project):
    simple_vote = owner.deploy(project.SimpleVote)
    simple_vote.register_voter(voter, sender=owner)
    assert simple_vote.voters(voter).voted is False
    assert simple_vote.voters(voter).weight == 1
    assert simple_vote.voters(random).weight == 0


def test_register_voter_not_owner(owner, voter, project):
    simple_vote = owner.deploy(project.SimpleVote)
    with ape.reverts():
        simple_vote.register_voter(voter, sender=voter)


def test_vote(owner, voter, candidate, project):
    simple_vote = owner.deploy(project.SimpleVote)
    simple_vote.register_voter(voter, sender=owner)
    simple_vote.add_candidate(candidate, "New Candidate", sender=owner)
    simple_vote.vote(candidate, sender=voter)
    assert simple_vote.candidates(candidate).vote_count == 1
    assert simple_vote.voters(voter).voted is True


def test_vote_not_registerd(owner, random, candidate, project):
    simple_vote = owner.deploy(project.SimpleVote)
    simple_vote.add_candidate(candidate, "New Candidate", sender=owner)
    with ape.reverts():
        simple_vote.vote(candidate, sender=random)


def test_cannot_vote_twice(owner, voter, candidate, project):
    simple_vote = owner.deploy(project.SimpleVote)
    simple_vote.register_voter(voter, sender=owner)
    simple_vote.add_candidate(candidate, "New Candidate", sender=owner)
    simple_vote.vote(candidate, sender=voter)
    with ape.reverts():
        simple_vote.vote(candidate, sender=voter)
