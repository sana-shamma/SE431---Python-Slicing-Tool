#include <stdio.h>
typedef struct {
    int arrivalTime;
    int burstTime;
    int startTime;
    int endTime;
    int waitTime;
    int turnaroundTime;
    int id;
} Process;
void calculateTimes(Process processes[], int numProcesses) {
    for (int i = 0; i < numProcesses - 1; i++) {
        for (int j = 0; j < numProcesses - i - 1; j++) {
            if (processes[j].arrivalTime > processes[j + 1].arrivalTime) {
                Process temp = processes[j];
                processes[j] = processes[j + 1];
                processes[j + 1] = temp;}}}
    int currentTime = 0;
    for (int i = 0; i < numProcesses; i++) {
        if (currentTime < processes[i].arrivalTime)
            currentTime = processes[i].arrivalTime;
        processes[i].startTime = currentTime;
        currentTime += processes[i].burstTime;
        processes[i].endTime = currentTime;
        processes[i].turnaroundTime = processes[i].endTime - processes[i].arrivalTime;
        processes[i].waitTime = processes[i].startTime - processes[i].arrivalTime;}}
int main() {
    int numProcesses;
    printf("Enter the number of processes: ");
    scanf("%d", &numProcesses);
    Process processes[numProcesses];
    int totalTurnaroundTime = 0, totalWaitTime = 0;
    for (int i = 0; i < numProcesses; i++) {
        printf("\nEnter the arrival time for process %d: ", i + 1);
        scanf("%d", &processes[i].arrivalTime);
        printf("Enter the burst time for process %d: ", i + 1);
        scanf("%d", &processes[i].burstTime);
        processes[i].id = i + 1;}
    calculateTimes(processes, numProcesses);
    printf("\nProcess\tStart Time\tEnd Time\tTurnaround Time\tWaiting Time\n");
    for (int i = 0; i < numProcesses; i++) {
        printf("%d\t%d\t\t%d\t\t%d\t\t%d\n", processes[i].id, processes[i].startTime, processes[i].endTime, processes[i].turnaroundTime, processes[i].waitTime);
        totalTurnaroundTime += processes[i].turnaroundTime;
        totalWaitTime += processes[i].waitTime;}
    double averageTurnaroundTime = (double)totalTurnaroundTime / numProcesses;
    double averageWaitTime = (double)totalWaitTime / numProcesses;
    printf("\nAverage Turnaround Time: %.2lf\n", averageTurnaroundTime);
    printf("Average Waiting Time: %.2lf\n", averageWaitTime);
    return 0;}
