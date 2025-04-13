from Patient import Patient
from Procedure import Procedure

patient = Patient("Franklin", "D", "Roosevelt", "123 Apple Road",
                  "New York", "New York", "12345", "123-456-7890",
                  "Emergency Contact", "900-800-7000")

procedure1 = Procedure("Physical Exam", "04/13/2025", "Dr. Irvine", 250.00)
procedure2 = Procedure("X-Ray", "04/13/2025", "Dr. Jamison", 500.00)
procedure3 = Procedure("Blood Test", "04/13/2025", "Dr. Smith", 250.00)

print(patient.getFName() + patient.getMName() + patient.getLName() +
      patient.getAddress() + patient.getCity() + patient.getState() +
      patient.getZip() + patient.getEmergencyContactName() + patient.getEmergencyContactPhone())



print(procedure1.getProcedure() + procedure1.getDate() +
      procedure1.getName() + str(procedure1.getCharge()))

print(procedure2.getProcedure() + procedure2.getDate() +
      procedure2.getName() + str(procedure2.getCharge()))

print(procedure3.getProcedure() + procedure3.getDate() +
      procedure3.getName() + str(procedure3.getCharge()))

totalCharge = procedure1.getCharge() + procedure2.getCharge() + procedure3.getCharge()
print(totalCharge)

