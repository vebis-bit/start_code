//
//  RecepieView.swift
//  start_code
//
//  Created by Kristian Sæberg on 28/10/2023.
//

import SwiftUI

struct Item: Decodable {
    let ingredients: [String: Float]
}

struct RecepieView: View {
    @Binding var selectedItem: String
    @State private var item: Item?
    @State private var showingAlert = false

    var body: some View {
        NavigationView {
            if let item = item {
                VStack{
                    List {
                        Section(header: Text("Ingredienser")) {
                            ForEach(Array(item.ingredients), id: \.key) { key, value in
                                HStack{
                                    Text(String(key))
                                    Spacer()
                                    Text("\(String(value)) gram")
                                    Spacer()
                                    Button {
                                        addToShoppingCart(itemID: key, amt: value)
                                        showingAlert = true
                                    } label: {
                                        Image(systemName: "plus")
                                            .foregroundColor(.blue)
                                    }
                                    .alert("La til \(value)g av \(key) i handlelisten din", isPresented: $showingAlert) {
                                        Button("OK", role: .cancel) { }
                                    }
                                }
                            }
                        }
                        .navigationTitle(selectedItem)
                        Section(header: Text("Fremgangsmåte")) {
                            Text("Fremgangsmetoden må du faen meg finne sjæl, du klarer jo å lage \(selectedItem) da kompis. Jeg skal være ærlig med deg; APIen vi bruker gir oss ikke fremgangsmåten.")
                                .foregroundColor(.gray)
                                .font(.footnote)
                                .frame(maxWidth: .infinity, alignment: .center)
                            Button() {
                                //
                            }label: {
                                Label("Lag oppskriften", systemImage: "fork.knife")
                                    .font(.system(size: 25, weight: .bold, design: .rounded))
                                    .foregroundColor(.white)
                                    .frame(width: 300, height: 50)
                                    .background(
                                        RoundedRectangle(cornerRadius: 15, style: .continuous)
                                            .fill(.red)
                                    )
                            }
                            Text("Dette vil trekke fra ingrediensene fra lageret")
                                .foregroundColor(.gray)
                                .font(.footnote)
                                .frame(maxWidth: .infinity, alignment: .center)
                        }
                    }
                }
            } else {
                Text("Laster inn oppskriften...")
            }
        }.onAppear(){
            queryData(itemID: selectedItem)
        }
    }
    
    func createURL(itemID: String, queryParam: String, base: String) -> URL? {
        let baseURL = "http://127.0.0.1:8000\(base)/"
        let sanitizedItemID = itemID.replacingOccurrences(of: " ", with: "_")
        let urlString = "\(baseURL)\(sanitizedItemID)?query_param=\(queryParam)"

        return URL(string: urlString)
    }
    
    func queryData(itemID: String) {
        print("prøver query")
        if let url = createURL(itemID: itemID, queryParam: "none", base: "/recepies") {
            print(url.absoluteString)
            // Use this URL for your URLSession request
            URLSession.shared.dataTask(with: url) { data, response, error in
                guard let data = data else { return }
                do {
                    let decodedData = try JSONDecoder().decode(Item.self, from: data)
                    DispatchQueue.main.async {
                        self.item = decodedData
                    }
                } catch {
                    print("Fucked!")
                    print("Error decoding: \(error)")
                }
            }.resume()
        }
    }
    
    func addToShoppingCart(itemID: String, amt: Float) {
        print("prøver å legge til i shopping cart")
        if let url = createURL(itemID: itemID, queryParam: String(amt), base: "/putshitincart") {
            print(url.absoluteString)
            // Use this URL for your URLSession request
            URLSession.shared.dataTask(with: url) { data, response, error in
                guard let data = data else { return }
                do {
                    let decodedData = try JSONDecoder().decode(Item.self, from: data)
                    DispatchQueue.main.async {
                        self.item = decodedData
                    }
                } catch {
                    print("Fucked!")
                    print("Error decoding: \(error)")
                }
            }.resume()
        }
    }
}

struct RecepieView_Previews: PreviewProvider {
    static var previews: some View {
        RecepieView(selectedItem: .constant("cheese"))
    }
}
