import SwiftUI

struct MyData: Decodable {
    let listOne: [String:Float]
    let listTwo: [String]
    let listThree: [Float]
}

struct IngredientsView: View {
    @State private var myData: MyData?
    
    
    var body: some View {
        ZStack{
            VStack {
                if let data = myData {
                    List {
                        Text("Kjøleskap")
                            .frame(maxWidth: 350, maxHeight:300)
                            .shadow(color: .black, radius: 5)
                            .foregroundColor(.white)
                            .font(.system(size: 50, weight: .bold, design: .rounded))
                            .listRowBackground(
                                RoundedRectangle(cornerRadius: 5)
                                    .fill(.clear)
                            )
                        Section() {
                            ForEach(Array(data.listOne), id: \.key) { key, value in
                                HStack{
                                    Text(String(key))
                                    Spacer()
                                    Text("\(String(value)) g")
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
                    .background(Image("matvarer"))
                    .scrollContentBackground(.hidden)
                } else {
                    Text("Laster inn lageret...")
                }
            }
            .onAppear {
                fetchData()
                triggerSpecificActionWithParams()
            }

        }
    }
    
    func fetchData() {
        guard let url = URL(string: "http://127.0.0.1:8000/items") else { return }
        
        URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data else { return }
            
            do {
                let decodedData = try JSONDecoder().decode(MyData.self, from: data)
                DispatchQueue.main.async {
                    self.myData = decodedData
                }
            } catch {
                print("Error decoding: \(error)")
            }
        }.resume()
    }
    
    func triggerSpecificActionWithParams() {
        guard let url = URL(string: "http://127.0.0.1:8000/trigger_specific_action") else {
            print("Invalid URL")
            return
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        let parameters: [String: Any] = [
            "name": "Your Item Name",
            "description": "Your Item Description"
        ]
        
        // Convert parameters to JSON data
        guard let httpBody = try? JSONSerialization.data(withJSONObject: parameters, options: []) else {
            return
        }
        request.httpBody = httpBody
        
        URLSession.shared.dataTask(with: request) { data, response, error in
            if let data = data {
                if let responseString = String(data: data, encoding: .utf8) {
                    print("Response: \(responseString)")
                    // Handle success or any response from the backend
                }
            } else if let error = error {
                print("Request failed: \(error.localizedDescription)")
            }
        }.resume()
    }
}
