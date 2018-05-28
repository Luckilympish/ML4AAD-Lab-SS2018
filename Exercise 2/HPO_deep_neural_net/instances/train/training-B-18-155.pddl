(define (problem prob24642) (:domain dom)
(:objects
	depot0 depot1 depot2 depot3 depot4 distributor0 distributor1 distributor2 distributor3 truck0 truck1 truck2 truck3 pallet0 pallet1 pallet2 pallet3 pallet4 pallet5 pallet6 pallet7 pallet8 crate0 crate1 crate2 crate3 crate4 crate5 crate6 crate7 crate8 crate9 crate10 crate11 crate12 crate13 crate14 crate15 crate16 crate17 hoist0 hoist1 hoist2 hoist3 hoist4 hoist5 hoist6 hoist7 hoist8 )
(:init
	(pallet pallet0)
	(surface pallet0)
	(at pallet0 depot0)
	(clear crate17)
	(pallet pallet1)
	(surface pallet1)
	(at pallet1 depot1)
	(clear crate16)
	(pallet pallet2)
	(surface pallet2)
	(at pallet2 depot2)
	(clear pallet2)
	(pallet pallet3)
	(surface pallet3)
	(at pallet3 depot3)
	(clear crate0)
	(pallet pallet4)
	(surface pallet4)
	(at pallet4 depot4)
	(clear crate11)
	(pallet pallet5)
	(surface pallet5)
	(at pallet5 distributor0)
	(clear crate8)
	(pallet pallet6)
	(surface pallet6)
	(at pallet6 distributor1)
	(clear crate9)
	(pallet pallet7)
	(surface pallet7)
	(at pallet7 distributor2)
	(clear crate15)
	(pallet pallet8)
	(surface pallet8)
	(at pallet8 distributor3)
	(clear crate14)
	(truck truck0)
	(at truck0 distributor2)
	(truck truck1)
	(at truck1 depot1)
	(truck truck2)
	(at truck2 depot3)
	(truck truck3)
	(at truck3 distributor3)
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
	(at hoist4 depot4)
	(available hoist4)
	(hoist hoist5)
	(at hoist5 distributor0)
	(available hoist5)
	(hoist hoist6)
	(at hoist6 distributor1)
	(available hoist6)
	(hoist hoist7)
	(at hoist7 distributor2)
	(available hoist7)
	(hoist hoist8)
	(at hoist8 distributor3)
	(available hoist8)
	(crate crate0)
	(surface crate0)
	(at crate0 depot3)
	(on crate0 pallet3)
	(crate crate1)
	(surface crate1)
	(at crate1 distributor1)
	(on crate1 pallet6)
	(crate crate2)
	(surface crate2)
	(at crate2 distributor2)
	(on crate2 pallet7)
	(crate crate3)
	(surface crate3)
	(at crate3 distributor1)
	(on crate3 crate1)
	(crate crate4)
	(surface crate4)
	(at crate4 distributor2)
	(on crate4 crate2)
	(crate crate5)
	(surface crate5)
	(at crate5 distributor0)
	(on crate5 pallet5)
	(crate crate6)
	(surface crate6)
	(at crate6 depot4)
	(on crate6 pallet4)
	(crate crate7)
	(surface crate7)
	(at crate7 distributor2)
	(on crate7 crate4)
	(crate crate8)
	(surface crate8)
	(at crate8 distributor0)
	(on crate8 crate5)
	(crate crate9)
	(surface crate9)
	(at crate9 distributor1)
	(on crate9 crate3)
	(crate crate10)
	(surface crate10)
	(at crate10 distributor2)
	(on crate10 crate7)
	(crate crate11)
	(surface crate11)
	(at crate11 depot4)
	(on crate11 crate6)
	(crate crate12)
	(surface crate12)
	(at crate12 distributor2)
	(on crate12 crate10)
	(crate crate13)
	(surface crate13)
	(at crate13 depot0)
	(on crate13 pallet0)
	(crate crate14)
	(surface crate14)
	(at crate14 distributor3)
	(on crate14 pallet8)
	(crate crate15)
	(surface crate15)
	(at crate15 distributor2)
	(on crate15 crate12)
	(crate crate16)
	(surface crate16)
	(at crate16 depot1)
	(on crate16 pallet1)
	(crate crate17)
	(surface crate17)
	(at crate17 depot0)
	(on crate17 crate13)
	(place depot0)
	(place depot1)
	(place depot2)
	(place depot3)
	(place depot4)
	(place distributor0)
	(place distributor1)
	(place distributor2)
	(place distributor3)
)

(:goal (and
		(on crate0 pallet4)
		(on crate1 crate5)
		(on crate2 crate7)
		(on crate3 pallet3)
		(on crate4 pallet2)
		(on crate5 crate11)
		(on crate7 crate13)
		(on crate8 crate16)
		(on crate11 pallet8)
		(on crate12 crate8)
		(on crate13 pallet5)
		(on crate14 crate12)
		(on crate15 crate1)
		(on crate16 crate4)
		(on crate17 pallet7)
	)
))
