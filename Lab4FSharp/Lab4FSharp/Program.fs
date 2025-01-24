// Zadanie 1
open System

type User = {
    Weight : float
    Height : float
    
}

let calculateBMI user =

    user.Weight/(user.Height * user.Height)

let classifyBMI bmi =

    match bmi with
    | x when x  < 18.5 -> "Niedowaga "
    | x when x < 25.0 -> "waga normalna"
    | x when x < 30.0 -> "nadwaga "
    | _ -> "Otyłość"

[<EntryPoint>]
let main argv =
    printfn "Podaj swoją wagę w kilogramach: "

    let weight = Console.ReadLine() |> float
    printfn "Podaj swój wzrost w metrach: "

    let height = Console.ReadLine() |> float

    let user = { Weight = weight; Height = height }
    let bmi = calculateBMI user
    let category = classifyBMI bmi

    printfn "Twoje BMI wynosi %.2f i jest klasyfikowane jako %s" bmi category
    0 

//Zadanie 2
open System
open System.Collections.Generic

let kursyWymiany = dict [

    ("USD", "EUR", 0.91)
    ("EUR", "USD", 1.10)
    ("GBP", "USD", 1.23)
    ("USD", "GBP", 0.81)
    ("EUR", "GBP", 0.89)
    ("GBP", "EUR", 1.12)

]

let przeliczWalute kwota walutaZrodlowa walutaDocelowa =

    let kurs = kursyWymiany.[(walutaZrodlowa, walutaDocelowa)]
    kwota * kurs

[<EntryPoint>]

let main argv =

    printfn "Wprowadź kwotę do przeliczenia: "
    let kwota = Console.ReadLine() |> float

    printfn "Wprowadź walutę źródłową: "
    let walutaZrodlowa = Console.ReadLine()

    printfn "Wprowadź walutę docelową: "
    let walutaDocelowa = Console.ReadLine()

    let przeliczonaKwota = przeliczWalute kwota walutaZrodlowa walutaDocelowa
    
    printfn "Przeliczona kwota: %.2f %s" przeliczonaKwota walutaDocelowa
    0

//Zadanie 3
open System
open System.Linq

let policzSlowa (tekst: string) =

    tekst.Split([| ' '; ','; '.'; ':'; '\t' |], 
    StringSplitOptions.RemoveEmptyEntries).Length

let policzZnaki (tekst: string) =

    tekst.Replace(" ", "").Length

let znajdzNajczestszeSlowo (tekst: string) =

    tekst.ToLower().Split([| ' '; ','; '.'; ':'; '\t' |], 
    StringSplitOptions.RemoveEmptyEntries)


    |> Seq.groupBy id
    |> Seq.map (fun (slowo, wystapienia) -> (slowo, Seq.length wystapienia))
    |> Seq.maxBy snd
    |> fst

[<EntryPoint>]
let main argv =

    printfn "Wprowadź tekst do analizy: "
    let tekst = Console.ReadLine()

    let liczbaSlow = policzSlowa tekst
    let liczbaZnakow = policzZnaki tekst
    let najczestszeSlowo = znajdzNajczestszeSlowo tekst

    printfn "Liczba słów: %d" liczbaSlow
    printfn "Liczba znaków (bez spacji): %d" liczbaZnakow
    printfn "Najczęstsze słowo: %s" najczestszeSlowo
    0

//Zadanie 5
open System

let board = Array.create 9 " "

let printBoard () =
    printfn "\n %s | %s | %s " board.[0] board.[1] board.[2]
    printfn "---+---+---"
    printfn " %s | %s | %s " board.[3] board.[4] board.[5]
    printfn "---+---+---"
    printfn " %s | %s | %s \n" board.[6] board.[7] board.[8]

let checkWin () =

    let lines = [(0,1,2); (3,4,5); (6,7,8); (0,3,6); (1,4,7); (2,5,8); (0,4,8); (2,4,6)]
    lines |> List.exists (fun (a, b, c) -> 

        if board.[a] <> " " && board.[a] = board.[b] && board.[b] = board.[c] then

            printfn "Wygrał %s!" board.[a]
            true
        else false)

let makeMove (player : string) =

    let mutable valid = false
    while not valid do

        printf "Ruch gracza %s (0-8): " player
        let input = Console.ReadLine()

        if Int32.TryParse(input, &_) && input.Length = 1 && board.[int input].[0] = ' ' then
            board.[int input] <- player
            valid <- true
        else
            printfn "Niepoprawny ruch, spróbuj ponownie."

let gameLoop () =

    let mutable turn = 0
    while not (checkWin() || turn = 9) do
        printBoard()
        
        if turn % 2 = 0 then
            makeMove "X"
        else
            makeMove "O"
        turn <- turn + 1


    if turn = 9 && not (checkWin()) then

        printfn "Remis!"


[<EntryPoint>]

let main argv =
    gameLoop()
    0