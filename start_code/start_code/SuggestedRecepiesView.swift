import SwiftUI

struct suggestedRecepiesData: Decodable {
    let names: [String:String]
}


struct SuggestedRecepiesView: View {
    @State private var resDat: suggestedRecepiesData?
    @State private var suggestDat: suggestedRecepiesData?

    @State private var isShowRecepie = false
    @State public var selectedItem: String = ""

    var body: some View {
        VStack {
            if let data = resDat {
                List {
                    Text("Dette kan du lage:")
                        .shadow(color: .black, radius: 5)
                        .frame(maxWidth: 350, maxHeight:300)
                        .foregroundColor(.white)
                        .font(.system(size: 30, weight: .bold, design: .rounded))
                        .listRowBackground(
                            RoundedRectangle(cornerRadius: 5)
                                .fill(.clear)
                        )
                    
                    Section() {
                        ForEach(Array(data.names), id: \.key) { key, value in
                            HStack{
                                Text(value)
                                Spacer()
                                Button {
                                    print(key)
                                    selectedItem = key
                                    print("Trykket på knapp")
                                    isShowRecepie.toggle()
                                } label: {
                                    Image(systemName: "arrow.forward")
                                }
                                .buttonStyle(.bordered)
                                
                            }
                            .listRowBackground(
                                RoundedRectangle(cornerRadius: 5)
                                    .fill(Color.white)
                                    .padding(2)
                            )
                            .listRowSeparator(.hidden)
                        }
                    }
                    
                    if let susDat = suggestDat {
                        Text("Skal du på butikken? Vi foreslår:")
                            .shadow(color: .black, radius: 5)
                            .padding(.top, 30)
                            .frame(maxWidth: 350, maxHeight:300)
                            .foregroundColor(.white)
                            .font(.system(size: 30, weight: .bold, design: .rounded))
                            .listRowBackground(
                                RoundedRectangle(cornerRadius: 5)
                                    .fill(.clear)
                            )
                        
                        Section() {
                            ForEach(Array(susDat.names), id: \.key) { key, value in
                                HStack{
                                    Text(value)
                                    Spacer()
                                    Button {
                                        print(key)
                                        selectedItem = key
                                        print("Trykket på knapp")
                                        isShowRecepie.toggle()
                                    } label: {
                                        Image(systemName: "arrow.forward")
                                    }
                                    .buttonStyle(.bordered)
                                }
                            }
                            .listRowBackground(
                                RoundedRectangle(cornerRadius: 5)
                                    .fill(Color.white)
                                    .padding(2)
                            )
                            .listRowSeparator(.hidden)
                        }
                    }
                }

                .sheet(isPresented: $isShowRecepie) {
                    RecepieView(selectedItem: $selectedItem)
                }
                .background(Image("Oppskrifter")
                    .resizable()
                    .scaledToFill()
                    .ignoresSafeArea()
                )
                .scrollContentBackground(.hidden)
            } else {
                Text("Laster inn lageret...")
            }
        }
        .onAppear {
            fetchData()
            fetchSuggestedData()
        }
    }

    func fetchData() {
        guard let url = URL(string: "http://127.0.0.1:8000/ablerecepiesIds") else { return }

        URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data else { return }
            print(data)
            do {
                let decodedData = try JSONDecoder().decode(suggestedRecepiesData.self, from: data)
                DispatchQueue.main.async {
                    self.resDat = decodedData
                }
            } catch {
                print("Error decoding: \(error)")
            }
        }.resume()
    }
    
    func fetchSuggestedData() {
        guard let url = URL(string: "http://127.0.0.1:8000/suggestedRecepies") else { return }

        URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data else { return }
            print(data)
            do {
                let decodedData = try JSONDecoder().decode(suggestedRecepiesData.self, from: data)
                DispatchQueue.main.async {
                    self.suggestDat = decodedData
                }
            } catch {
                print("Error decoding: \(error)")
            }
        }.resume()
    }
}

struct SuggestedRecepiesView_Previews: PreviewProvider {
    static var previews: some View {
        SuggestedRecepiesView()
    }
}
