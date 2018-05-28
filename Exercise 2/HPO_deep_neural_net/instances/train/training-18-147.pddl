(define (problem prob561) (:domain dom)
(:objects
	depot0 depot1 depot2 depot3 distributor0 distributor1 distributor2 truck0 truck1 truck2 pallet0 pallet1 pallet2 pallet3 pallet4 pallet5 pallet6 crate0 crate1 crate2 crate3 crate4 crate5 crate6 crate7 crate8 crate9 crate10 crate11 crate12 crate13 crate14 crate15 crate16 crate17 hoist0 hoist1 hoist2 hoist3 hoist4 hoist5 hoist6 )
(:init
	(pallet pallet0)
	(surface pallet0)
	(at pallet0 depot0)
	(clear crate13)
	(pallet pallet1)
	(surface pallet1)
	(at pallet1 depot1)
	(clear crate12)
	(pallet pallet2)
	(surface pallet2)
	(at pallet2 depot2)
	(clear crate6)
	(pallet pallet3)
	(surface pallet3)
	(at pallet3 depot3)
	(clear crate8)
	(pallet pallet4)
	(surface pallet4)
	(at pallet4 distributor0)
	(clear crate16)
	(pallet pallet5)
	(surface pallet5)
	(at pallet5 distributor1)
	(clear pallet5)
	(pallet pallet6)
	(surface pallet6)
	(at pallet6 distributor2)
	(clear crate17)
	(truck truck0)
	(at truck0 distributor1)
	(truck truck1)
	(at truck1 depot2)
	(truck truck2)
	(at truck2 depot1)
	(hoist hoist0)
	(at hoist0 depot0)
	(available hoist0)
	(hoist hoist1)
	(at hoist1 depot1)
	(available hoist1)
	(hoist hoist2)
	(at hoist2 depot2)
	(available hoist2)
	(hoist hoist3)
	(at hoist3 depot3)
	(available hoist3)
	(hoist hoist4)
	(at hoist4 distributor0)
	(available hoist4)
	(hoist hoist5)
	(at hoist5 distributor1)
	(available hoist5)
	(hoist hoist6)
	(at hoist6 distributor2)
	(available hoist6)
	(crate crate0)
	(surface crate0)
	(at crate0 depot2)
	(on crate0 pallet2)
	(crate crate1)
	(surface crate1)
	(at crate1 depot1)
	(on crate1 pallet1)
	(crate crate2)
	(surface crate2)
	(at crate2 depot0)
	(on crate2 pallet0)
	(crate crate3)
	(surface crate3)
	(at crate3 distributor2)
	(on crate3 pallet6)
	(crate crate4)
	(surface crate4)
	(at crate4 depot1)
	(on crate4 crate1)
	(crate crate5)
	(surface crate5)
	(at crate5 depot1)
	(on crate5 crate4)
	(crate crate6)
	(surface crate6)
	(at crate6 depot2)
	(on crate6 crate0)
	(crate crate7)
	(surface crate7)
	(at crate7 distributor0)
	(on crate7 pallet4)
	(crate crate8)
	(surface crate8)
	(at crate8 depot3)
	(on crate8 pallet3)
	(crate crate9)
	(surface crate9)
	(at crate9 distributor0)
	(on crate9 crate7)
	(crate crate10)
	(surface crate10)
	(at crate10 distributor0)
	(on crate10 crate9)
	(crate crate11)
	(surface crate11)
	(at crate11 depot1)
	(on crate11 crate5)
	(crate crate12)
	(surface crate12)
	(at crate12 depot1)
	(on crate12 crate11)
	(crate crate13)
	(surface crate13)
	(at crate13 depot0)
	(on crate13 crate2)
	(crate crate14)
	(surface crate14)
	(at crate14 distributor0)
	(on crate14 crate10)
	(crate crate15)
	(surface crate15)
	(at crate15 distributor2)
	(on crate15 crate3)
	(crate crate16)
	(surface crate16)
	(at crate16 distributor0)
	(on crate16 crate14)
	(crate crate17)
	(surface crate17)
	(at crate17 distributor2)
	(on crate17 crate15)
	(place depot0)
	(place depot1)
	(place depot2)
	(place depot3)
	(place distributor0)
	(place distributor1)
	(place distributor2)
)

(:goal (and
		(on crate0 crate3)
		(on crate1 crate10)
		(on crate2 pallet1)
		(on crate3 pallet4)
		(on crate4 pallet2)
		(on crate5 crate2)
		(on crate7 pallet6)
		(on crate8 crate7)
		(on crate9 crate15)
		(on crate10 pallet3)
		(on crate11 pallet5)
		(on crate12 crate17)
		(on crate15 crate11)
		(on crate17 pallet0)
	)
))
