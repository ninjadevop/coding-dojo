const pokémon = Object.freeze([
        { "id": 1,   "name": "Bulbasaur",  "types": ["poison", "grass"] },
        { "id": 5,   "name": "Charmeleon", "types": ["fire"] },
        { "id": 9,   "name": "Blastoise",  "types": ["water"] },
        { "id": 12,  "name": "Butterfree", "types": ["bug", "flying"] },
        { "id": 16,  "name": "Pidgey",     "types": ["normal", "flying"] },
        { "id": 23,  "name": "Ekans",      "types": ["poison"] },
        { "id": 24,  "name": "Arbok",      "types": ["poison"] },
        { "id": 25,  "name": "Pikachu",    "types": ["electric"] },
        { "id": 37,  "name": "Vulpix",     "types": ["fire"] },
        { "id": 52,  "name": "Meowth",     "types": ["normal"] },
        { "id": 63,  "name": "Abra",       "types": ["psychic"] },
        { "id": 67,  "name": "Machamp",    "types": ["fighting"] },
        { "id": 72,  "name": "Tentacool",  "types": ["water", "poison"] },
        { "id": 74,  "name": "Geodude",    "types": ["rock", "ground"] },
        { "id": 87,  "name": "Dewgong",    "types": ["water", "ice"] },
        { "id": 98,  "name": "Krabby",     "types": ["water"] },
        { "id": 115, "name": "Kangaskhan", "types": ["normal"] },
        { "id": 122, "name": "Mr. Mime",   "types": ["psychic"] },
        { "id": 133, "name": "Eevee",      "types": ["normal"] },
        { "id": 144, "name": "Articuno",   "types": ["ice", "flying"] },
        { "id": 145, "name": "Zapdos",     "types": ["electric", "flying"] },
        { "id": 146, "name": "Moltres",    "types": ["fire", "flying"] },
        { "id": 148, "name": "Dragonair",  "types": ["dragon"] }
    ]);

    
    // !===========1================
    const pokemon_d=pokémon.filter((p) => {
        return p.id%3==0
    })
    // console.log(pokemon_d);
// !===========2================
    const pokemon_type=pokémon.filter((p) => {
        return p.types=="fire"
    })
    // console.log(pokemon_type);
// !===========3================
    const pokemon_ty=pokémon.filter((p) => {
        return p.types.length>1
    })
// console.log(pokemon_ty);
// !===========4================
const pokemon_name=pokémon.map((p) => {
    return p.name
})
// console.log(pokemon_name);
// !===========5================
const pokemon_nam=pokémon.filter((p) => {
    return p.id>99
}).map((p)=> {
    return p.name
})
// console.log(pokemon_nam);
// !===========6================
const pokemon_poi=pokémon.filter((p) => {
    return p.types.includes("poison")
}).map((p)=> {
    return p.name
})
// console.log(pokemon_poi);
// !===========7================
const pokemon=pokémon.filter((p) => {
    return p.types[1]=="flying"
}).map((p)=> {
    return p.types[0]
})
// console.log(pokemon);
// !===========8================
const pokemon_count=pokémon.filter((p) => {
    return p.types.includes("normal")
}).length
console.log(pokemon_count);