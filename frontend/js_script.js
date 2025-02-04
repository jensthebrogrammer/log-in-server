const logData = async (event) => {    // asynchroon omdat we moeten wachten op de response van de backend
  event.preventDefault()    // zorgt ervoor dat je niet automatisch refreshed

  // haal alle ingevulde data op
  const userName = document.getElementById('userName').value || null    // || null is er om duidelijk te maken wanneer er niks is ingevuld
  const password = document.getElementById('pasword').value || null
  const maleInput = document.getElementById('male').checked && "male"   // als het aangeduid is is de const = "male"
  const femaleInput = document.getElementById('female').checked && "female"
  const nothingInput = document.getElementById('nothing').checked && "will not say"
  const age = document.getElementById('age').value || null

  // kijken of alles is ingevuld
  if ([userName, password, age].includes(null)) {
    alert("must fill in all fields")
    return
  }

  // kijken welke vakjes er zijn aangeduid
  let gender = []
  const temp = [maleInput, femaleInput, nothingInput]
  temp.forEach((x) => {
    if (x) {
      gender.push(x)
    }
  })

  // nakijken hoeveel vakjes er zijn aangeduid
  if (gender.length != 1) {
    alert("something is wrong in the checkboxes")
    return
  } else {
    gender = gender[0]    // uit de lijst halen
  }

  // nakijken of age wel echt een getal is (niet optimaal)
  let brk = false
  age.split("").forEach((element) => {
    if (!brk) {
      if (["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"].includes(element)) {
        null
      } else {
        alert("must fill in a number")
        brk = true
      }
    }
  })

  // als het niet klopt gaat hij terug
  // dit word op deze manier gedaan omdat je in de loop niet kan returnen
  // anders return hij meerdere keren
  if (brk) {
    return
  }

  // nakijken of je niet te oud of jong bent
  if (Number(age) < 12 || Number(age) > 80) {
    alert("you are to old/young for this site")
    return 
  }

  console.log(userName)
  console.log(password)
  console.log(age)
  console.log(gender)

  // data die naar de backend gaat
  const data = {
    userName,
    password,
    age,
    gender
  }

  // in de juiste format steken
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data)
  }

  // versturen naar de backend
  const url = "http://127.0.0.1:5000/post_new_user"
  const response = await fetch(url, options)

  // de response nakijken
  if (response.status !== 200) {
    const data = await response.json();
    alert(data.message);
  } else {
    // refreshen
    window.location.reload();
  }
}
